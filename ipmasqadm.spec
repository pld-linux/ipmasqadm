Summary:	Ipmasqadm utility
Summary(pl):	Narzêdzie ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	1d
Vendor:		Juan Jose Ciarlante <irriga@impsat1.com.ar>
Copyright:	distributable
Group:		Networking/Admin
Group(pl):	Sieæ/Administracja
Source:		http://juanjox.home.ml.org/ipmasqadm-%{version}.tar.gz
Patch:		%{name}-%{version}.make.diff
BuildRoot:	/var/tmp/buildroot-%{name}-%{version}

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

strip		$RPM_BUILD_ROOT/usr/sbin/ipmasqadm
bzip2 -9	$RPM_BUILD_ROOT/usr/man/man8/* doc/* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ChangeLog.bz2

%attr(700,root,root) /usr/sbin/ipmasqadm

%attr(700,root,root) %dir /usr/lib/ipmasqadm
%attr(755,root,root) /usr/lib/ipmasqadm/*.so

%attr(644,root, man) /usr/man/man8/*

%changelog
* Sat Jan 23 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.4.2-1d]
- new upstream release for newest 2.2 kernels
