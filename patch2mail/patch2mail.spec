#
Name:           patch2mail
Version:        1.0
Release:        1
#
License:        GPLv2+
#
Summary:        Patch notification via mail
#BuildRequires: bash
#
Url:            http://blog.cboltz.de/plugin/tag/patch2mail
Group:          System/Packages
Source:         %{name}-%{version}.tar.bz2
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:       /bin/hostname
Requires:       /bin/rm
Requires:       /usr/bin/xsltproc
Requires:       cron
Requires:       grep
Requires:       mail
Requires:       mktemp
Requires:       zypper
# detailed requirements:
#      zypper    # (>= 11.0) zypp-refresh-rapper, zypper
#      zypper    # (<= 10.3) zypp-checkpatches-wrapper
#      libxslt   # xsltproc [NOT autodetected, even if rpmlint thinks so]
#      coreutils # rm
#      net-tools # hostname

%description
patch2mail checks for available updates and sends a mail to root
if any patches are available

%prep
%setup -q

%build

%install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -d -m 0755 %{buildroot}%{_localstatedir}/adm/fillup-templates/

%{__install} -m 0644 patch2mail.xsl %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%if 0%{?suse_version} < 1030
	%{__install} -m 0644 patch2mail.xsl_10.2 %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%endif

%{__install} -m 0755 patch2mail %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%if 0%{?suse_version} < 1110
	%{__install} -m 0755 patch2mail_11.0 %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%endif
%if 0%{?suse_version} < 1100
	%{__install} -m 0755 patch2mail_10.3 %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%endif
%{__install} -m 0644 patch2mail.sysconfig %{buildroot}%{_localstatedir}/adm/fillup-templates/sysconfig.patch2mail

echo ==== Buildroot: %{buildroot} ====
find %{buildroot}
echo ================================

%clean
%{__rm} -rf %{buildroot}

%post
%{fillup_only -n patch2mail}

%files
%defattr(-,root,root)
%{_sysconfdir}/cron.daily/%{name}
%{_datadir}/%{name}
%{_localstatedir}/adm/fillup-templates/sysconfig.patch2mail
%doc README COPYING

%changelog
