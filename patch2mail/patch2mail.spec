# norootforbuild
#
Name:          patch2mail
Version:       0.9.1
Release:       1
#
License:       GPL
Group:         System/Packages
#
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: bash
#
URL:           http://www.cboltz.de
Source:        %{name}-%{version}.tar.bz2
#
Summary:       patch2mail - patch notification via mail
BuildArch:     noarch

Requires:      bash mktemp mail grep zypper libxslt coreutils net-tools
# detailed requirements:
#      zypper # zypp-checkpatches-wrapper
#      libxslt # xsltproc
#      coreutils # rm
#      net-tools # hostname

%description
patch2mail checks zypp-checkpatches-wrapper for available
updates and sends a mail to root if any patches are available

Authors:
----------
    Christian Boltz < p a c k a g e s  AT  c b o l t z DOT d e >

%prep
%setup

%build

%install
%{__mkdir} -p %{buildroot}/usr/share/%{name}

%if 0%{?suse_version} < 1030
	%{__cp} patch2mail.xsl_10.2 %{buildroot}/usr/share/%{name}/patch2mail.xsl
%else
	%{__cp} patch2mail.xsl %{buildroot}/usr/share/%{name}/
%endif

%{__mkdir} -p %{buildroot}/etc/cron.daily
%{__cp} patch2mail %{buildroot}/etc/cron.daily/

echo === Buildroot: %{buildroot} ===
find %{buildroot}
echo ================================

%clean

%files
%defattr(-,root,root)
%attr(755, root, root) /etc/cron.daily/%{name}
/usr/share/%{name}/
/usr/share/%{name}/%{name}.xsl

