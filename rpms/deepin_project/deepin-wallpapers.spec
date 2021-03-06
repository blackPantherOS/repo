%global _commit dbc981b0f6b2b63d681fba8ff361e11ea226fc00
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-wallpapers
Version:        1.3
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Deepin Wallpapers provides wallpapers of dde
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{_commit}/%{name}-%{_shortcommit}.tar.gz
BuildArch:      noarch

%description
Deepin Wallpapers provides wallpapers of dde

%prep
%setup -q -n %{name}-%{_commit}

%build

%install
install -d %{buildroot}/%{_datadir}/wallpapers/
cp -r deepin %{buildroot}/%{_datadir}/wallpapers/

install -d %{buildroot}/%{_var}/cache/
cp -r image-blur %{buildroot}/%{_var}/cache/

%files
%doc README.md
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.gitdbc981b
- Update to 1.3
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
