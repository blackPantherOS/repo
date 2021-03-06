%global _commit 8692ad3b17fe98291110d6135796ba652521cc9e
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-wm-switcher
Version:        1.1.0
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Window manager switcher for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wm-switcher
Source0:        %{url}/archive/%{_commit}/%{name}-%{_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       deepin-daemon
Requires:       deepin-wm
Requires:       deepin-metacity

%description
Window manager switcher for Deepin

%prep
%setup -q -n %{name}-%{_commit}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.1.0-1.git8692ad3
- Update to 1.1.0
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Initial package build
