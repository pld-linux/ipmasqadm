Summary:	Ipmasqadm utility
Summary(pl):	Narz�dzie ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	2
Copyright:	distributable
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	http://juanjox.kernelnotes.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.make.diff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows ipmasq addtional setup, it is needed if you want to
activate port forwarding or auto forwarding in 2.2 kernels.

%description -l pl
To narz�dzie pozwala na aktywowanie forwardowania port�w lub
automatycznego forwardowania w kernelach 2.2.

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	%{name} for bootdisk
Group:		Applications/System
%description BOOT
%endif

%prep
%setup -q
%patch -p1

%build

%if %{?BOOT:1}%{!?BOOT:0}
%{__make} \
	OPT="-Os" \
	XCFLAGS="-I%{_libdir}/bootdisk%{_includedir}" \
	KSRC=%{_prefix}/src/linux \
	LDFLAGS="-nostdlib -s -L../lib" \
	LDLIBS='$(SH_LDLIBS) -lgcc' \
	SH_LDLIBS="-lip_masq \
		%{_libdir}/bootdisk%{_libdir}/libdl.a \
		%{_libdir}/bootdisk%{_libdir}/crt0.o \
		%{_libdir}/bootdisk%{_libdir}/libc.a"
mv -f %{name}/%{name} %{name}-BOOT
%{__make} clean
%endif


%{__make} OPT="%{rpmcflags}" KSRC=%{_prefix}/src/linux

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin
for i in *-BOOT; do 
  install -s $i $RPM_BUILD_ROOT/usr/lib/bootdisk/sbin/`basename $i -BOOT`
done
%endif


install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/ipmasqadm} 

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

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/sbin/*
%endif
