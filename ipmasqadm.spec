Summary:	Ipmasqadm utility
Summary(pl):	Narzêdzie ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	2
Copyright:	distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Source:		http://juanjox.home.ml.org/ipmasqadm-%{version}.tar.gz
Patch:		%{name}-%{version}.make.diff
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This tool allows ipmasq addtional setup, it is needed if you 
want to activate port forwarding or auto forwarding in 2.2 kernels.

%description -l pl
To narzêdzie pozwala na aktywowanie forwardowania portów
lub automatycznego forwardowania w kernelach 2.2.

%prep
%setup -q
%patch -p1

%build
make OPT="$RPM_OPT_FLAGS" KSRC=/usr/src/linux 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{sbin,lib/ipmasqadm} 

make DESTDIR=$RPM_BUILD_ROOT install

strip		$RPM_BUILD_ROOT%{_sbindir}/ipmasqadm
gzip -9nf	$RPM_BUILD_ROOT%{_mandir}/man8/* doc/* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ChangeLog.gz

%attr(700,root,root) %{_sbindir}/ipmasqadm

%attr(700,root,root) %dir %{_libdir}/ipmasqadm
%attr(755,root,root) %{_libdir}/ipmasqadm/*.so

%{_mandir}/man8/*
