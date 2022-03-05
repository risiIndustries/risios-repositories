Name:		risios-repositories
Version:	35
Release:	3%{?dist}
Summary:	Repository files for searchable repositories

License:	GPL
URL:		  https://github.com/risiOS/risios-repositories
Source0:	https://github.com/risiOS/risios-repositories/archive/refs/heads/main.tar.gz#/risios-repositories-main.tar.gz

BuildArch:	noarch

Provides:	fedora-workstation-repositories
# For rpmfusions-nonfree repo keys
Requires:	distribution-gpg-keys
Requires:       fedora-third-party
# For /etc/yum.repos.d
Requires:	fedora-repos

%description
Repository files that make some select non-Fedora software available
via search in gnome-software.

%prep
%autosetup -n risios-repositories-main

%build
%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d
cp yum.repos.d/* $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp risios.conf $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d/

%files
%{_prefix}/lib/fedora-third-party/conf.d/*.conf
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Wed Mar 2 2022 PizzaLovingNerd <pizzalovingnerd@teknik.io> - 35-1
- Removed third-party repos in favor of risi-script

* Sun Nov 14 2021 PizzaLovingNerd <pizzalovingnerd@teknik.io> - 35-1
- risiOS
- Adds a bunch of extra repos and full rpmfusion

* Mon Aug 2 2021 Owen Taylor <otaylor@redhat.com> - 35-1
- https://fedoraproject.org/wiki/Changes/Third_Party_Software_Mechanism

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 32-2
- Temporarily revert filtered flathub remote

* Fri Oct 04 2019 Matthias Clasen <mclasen@redhat.com> - 32-1
- Add a filtered flathub remote

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 31-1
- Add skip_if_unavailable=True to all third party repos (#1750414)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-1
- Make repo files %%config(noreplace) so they aren't clobbered on upgrade if
  they have been modified (such as being enabled).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 28-1
- Add rpmfusion-nonfree-nvidia-driver.repo and rpmfusion-nonfree-steam.repo

* Thu Apr 05 2018 Kalev Lember <klember@redhat.com> - 25-5
- Add URL that points to a Workstation third party software wiki page

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Matthias Clasen <mclasen@redhat.com> - 25-1
- Add the Google Chrome repository

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun  8 2015 Matthias Clasen <mclasen@redhat.com>
- Initial packaging

