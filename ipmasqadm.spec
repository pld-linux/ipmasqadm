Summary:	Ipmasqadm utility
Summary(pl):	Narzêdzie ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	2
Copyright:	distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Source0:	http://juanjox.kernelnotes.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.make.diff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows ipmasq addtional setup, it is needed if you want to
activate port forwarding or auto forwarding in 2.2 kernels.

%description -l pl
To narzêdzie pozwala na aktywowanie forwardowania portów lub
automatycznego forwardowania w kernelach 2.2.

%prep
%setup -q
%patch -p1

%build
%{__make} OPT="$RPM_OPT_FLAGS" KSRC=%{_prefix}/src/linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/ipmasqadm} 

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT/%{_mandir}

strip $RPM_BUILD_ROOT%{_sbindir}/ipmasqadm

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* doc/* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ChangeLog.gz

%attr(700,root,root) %{_sbindir}/ipmasqadm

%attr(700,root,root) %dir %{_libdir}/ipmasqadm
%attr(755,root,root) %{_libdir}/ipmasqadm/*.so

%{_mandir}/man8/*
