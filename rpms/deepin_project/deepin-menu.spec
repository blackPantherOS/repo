%global _commit 3750b2f385c6e91978b3d03d5e571b626f3877a5
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-menu
Version:        3.0.10
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Deepin menu service

Group:          Development/Libraries
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-menu
Source0:        %{url}/archive/%{_commit}/%{name}-%{_shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel
Requires:       python-qt5

%description
Deepin menu service for building beautiful menus.

%prep
%setup -q -n %{name}-%{_commit}

# Remove python shebang
find -iname "*.py" | xargs sed -i '/env python/d'

# Modify lib path to reflect the platform
sed -i 's|/usr/lib|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

# Fix setup.py install path
sed -i '/data_files/s|list_files.*)|"")|' setup.py

%build
%{__python2} setup.py build
%{qmake_qt5} DEFINES+=QT_NO_DEBUG_OUTPUT
%{make_build}

%install
%{__python2} setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}
%{make_install} INSTALL_ROOT="%{buildroot}"

install -d %{buildroot}%{_datadir}/dbus-1/services/
install -m644 data/*.service %{buildroot}%{_datadir}/dbus-1/services/

install -d %{buildroot}%{_datadir}/applications/
desktop-file-install --remove-key=OnlyShowIn --mode=644 \
    --dir=%{buildroot}%{_datadir}/applications deepin-menu.desktop

install -d %{buildroot}/etc/xdg/autostart/
ln -sfv %{_datadir}/applications/%{name}.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libexecdir}/%{name}
%{python_sitelib}/deepin_menu*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.menu.service

%changelog
* Tue Feb 21 2017 mosquito <sensor.wen@gmail.com> - 3.0.10-1.git3750b2f
- Update to 3.0.10
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.7-1.git6038c51
- Update to 3.0.7
* Wed Jul 01 2015 mosquito <sensor.wen@gmail.com> - 2.90.0-1.git7557d46
- Update version to 2.90.0-1.git7557d46
* Wed Dec 03 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141202-1
- Update version to 1.1git20141202
* Mon Dec 01 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141124-1
- Update version to 1.1git20141124
* Tue Nov 18 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141113-1
- Update version to 1.1git20141113
* Tue Nov 4 2014 mosquito <sensor.wen@gmail.com> - 1.1git20141028-1
- Update version to 1.1git20141028
* Thu Oct 9 2014 mosquito <sensor.wen@gmail.com> - 1.1git20140923-2
- Fixed depends
* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 1.1git20140923-1
- Initial build
