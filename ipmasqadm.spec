Summary:	Ipmasqadm utility
Summary(es.UTF-8):	Utilitario ipmasqadm
Summary(pl.UTF-8):	Narzędzie ipmasqadm
Summary(pt_BR.UTF-8):	Utilitário ipmasqadm
Name:		ipmasqadm
Version:	0.4.2
Release:	5
License:	distributable
Group:		Networking/Admin
Source0:	http://www.e-infomax.com/ipmasq/juanjox/%{name}-%{version}.tar.gz
# Source0-md5:	85ea429e3617dcc99133d310476ff29a
Patch0:		%{name}-%{version}.make.diff
Patch1:		%{name}-no_dlopen.patch
URL:		http://www.e-infomax.com/ipmasq/juanjox/
BuildRequires:	kernel-headers < 2.3.0
Conflicts:	kernel >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows ipmasq addtional setup, it is needed if you want to
activate port forwarding or auto forwarding in 2.2 kernels.

%description -l es.UTF-8
Esta herramienta permite la configuración adicional de ipmasq, y puede
usarse en caso de que se desee activar una salida de reenvío y reenvío
automático.

%description -l pl.UTF-8
To narzędzie pozwala na aktywowanie forwardowania portów lub
automatycznego forwardowania w kernelach 2.2.

%description -l pt_BR.UTF-8
Essa ferramenta permite configuração adicional do ipmasq, e pode ser
usada caso você deseje ativar port forwarding e auto forwarding.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} OPT="%{rpmcflags}" KSRC=%{_kernelsrcdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/ipmasqadm}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ChangeLog
%attr(755,root,root) %{_sbindir}/ipmasqadm
%dir %{_libdir}/ipmasqadm
%attr(755,root,root) %{_libdir}/ipmasqadm/*.so
%{_mandir}/man8/*
