%define snapshot 20200409

Name:		plasma-mobile
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	Plasma interface for mobile devices
# git://anongit.kde.org/plasma-mobile
Source0:	plasma-mobile-%{snapshot}.tar.zst
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(PkgConfig)

%description
Plasma interface for mobile devices

%prep
%autosetup -p1 -n %{name}-%{snapshot}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/active-filebrowser
%{_libdir}/qt5/qml/org/kde/plasma/mobilecomponents
%{_datadir}/icons/*/*/*/*
%{_datadir}/kservices5/org.kde.active.audiopart.desktop
%{_datadir}/kservices5/org.kde.active.imageviewerpart.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.active.filebrowser.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.plasma.activecontainment.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.plasma.activepanel.desktop
%{_datadir}/kservices5/plasma-package-org.kde.plasma.activetoolbox.desktop
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.active.desktop
%{_datadir}/kservicetypes5/plasma-filebrowserpart.desktop
%{_datadir}/metainfo/org.kde.plasma.active.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activepanel.appdata.xml
%{_datadir}/plasma/packages/org.kde.active.audiopart
%{_datadir}/plasma/packages/org.kde.active.imageviewerpart
%{_datadir}/plasma/packages/org.kde.plasma.activetoolbox
%{_datadir}/plasma/plasmoids/org.kde.plasma.active.filebrowser
%{_datadir}/plasma/plasmoids/org.kde.plasma.activecontainment
%{_datadir}/plasma/plasmoids/org.kde.plasma.activepanel
%{_datadir}/plasma/shells/org.kde.plasma.active
%{_datadir}/solid/actions/browse-files.desktop
