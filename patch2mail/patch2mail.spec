# norootforbuild
#
Name:          patch2mail
Version:       0.9.3
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
Summary:       Patch notification via mail
BuildArch:     noarch

Requires:      bash mktemp mail grep zypper coreutils net-tools cron libxslt
# detailed requirements:
#      zypper    # (>= 11.0) zypp-refresh-rapper, zypper
#      zypper    # (<= 10.3) zypp-checkpatches-wrapper
#      libxslt   # xsltproc [NOT autodetected, even if rpmlint thinks so]
#      coreutils # rm
#      net-tools # hostname

%description
patch2mail checks for available updates and sends a mail to root
if any patches are available

Authors:
----------
    Christian Boltz < p a c k a g e s  AT  c b o l t z DOT d e >

%prep
%setup -q

%build

%install
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}/etc/cron.daily

%{__cp} patch2mail.xsl %{buildroot}%{_datadir}/%{name}/
%if 0%{?suse_version} < 1030
	%{__cp} patch2mail.xsl_10.2 %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%endif

%{__cp} patch2mail %{buildroot}/etc/cron.daily/
%if 0%{?suse_version} < 1110
	%{__cp} patch2mail_11.0 %{buildroot}/etc/cron.daily/patch2mail
%endif
%if 0%{?suse_version} < 1100
	%{__cp} patch2mail_10.3 %{buildroot}/etc/cron.daily/patch2mail
%endif

echo ==== Buildroot: %{buildroot} ====
find %{buildroot}
echo ================================

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755, root, root) /etc/cron.daily/%{name}
%{_datadir}/%{name}/
%{_datadir}/%{name}/%{name}.xsl
%doc README

%changelog
* Sun Jul 20 2008 - cboltz
- update for openSUSE 11.0 (scripts for older versions still included)
- version 0.9.2
* Mon Feb 18 2008 - cboltz
- Initial SVN commit of patch2mail
- SVN: http://svn.opensuse.org/svn/zypp/trunk/tools/patch2mail
- version 0.9.1

