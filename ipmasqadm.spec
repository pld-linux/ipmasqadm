# conditional build:
# _without_embed - don't build uClibc version
Summary:	Ipmasqadm utility
Summary(pl):	Narzêdzie ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	4
License:	distributable
Group:		Networking/Admin
Source0:	http://juanjox.kernelnotes.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.make.diff
Patch1:		%{name}-no_dlopen.patch
BuildRequires:	kernel-headers < 2.3.0
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif
Conflicts:	kernel >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

%description
This tool allows ipmasq addtional setup, it is needed if you want to
activate port forwarding or auto forwarding in 2.2 kernels.

%description -l pl
To narzêdzie pozwala na aktywowanie forwardowania portów lub
automatycznego forwardowania w kernelach 2.2.

%package embed
Summary:	ipmasqadm for bootdisk
Summary(pl):	ipmasqadm na bootkietkê
Group:		Applications/System

%description embed
ipmasqadm for bootdisk.

%description embed -l pl
ipmasqadm na bootkietkê.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%if %{!?_without_embed:1}%{?_without_embed:0}
%{__make} SUBDIRS="lib modules" \
	OPT="%{embed_cflags}" \
	XCFLAGS="-DNO_DLOPEN" \
	CC=%{embed_cc} \
	KSRC=%{_kernelsrcdir} \
	LDFLAGS="-L../lib" \
	SH_LDFLAGS="-L../lib"
mv -f %{name}/%{name} %{name}-embed-shared

%{__make} SUBDIRS="lib modules" \
	OPT="%{embed_cflags}" \
	XCFLAGS="-DNO_DLOPEN" \
	CC=%{embed_cc} \
	KSRC=%{_kernelsrcdir} \
	LDFLAGS="-static -L../lib" \
	SH_LDFLAGS="-static -L../lib"
mv -f %{name}/%{name} %{name}-embed-static

%{__make} clean
%endif

%{__make} OPT="%{rpmcflags}" KSRC=%{_kernelsrcdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/ipmasqadm}

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{embed_path}/{shared,static}
install %{name}-embed-shared $RPM_BUILD_ROOT%{embed_path}/shared/%{name}
install %{name}-embed-static $RPM_BUILD_ROOT%{embed_path}/static/%{name}
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf doc/* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ChangeLog.gz
%attr(755,root,root) %{_sbindir}/ipmasqadm
%dir %{_libdir}/ipmasqadm
%attr(755,root,root) %{_libdir}/ipmasqadm/*.so
%{_mandir}/man8/*

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/*
%endif
