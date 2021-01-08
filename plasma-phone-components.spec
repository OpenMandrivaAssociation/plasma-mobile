%define snapshot 20210108
%define commit 6204b90a5106e1a8acb1853efa0c8555d7c3097c

Name:		plasma-phone-components
Version:	0.0
Summary:	Plasma components for mobile phones
# https://invent.kde.org/plasma/plasma-phone-components
%if "%{?commit:%{commit}}" != ""
Source0:	https://invent.kde.org/plasma/plasma-phone-components/-/archive/%{commit}/plasma-phone-components-%{commit}.tar.bz2
Release:	0.%{snapshot}.%{commit}.1
%else
Source0:	https://invent.kde.org/plasma/plasma-phone-components/-/archive/master/plasma-phone-components-master.tar.bz2
Release:	0.%{snapshot}.1
%endif
Patch0:		plasma-phone-components-x11-session.patch
Patch1:		plasma-phone-components-no-dbus-run-session.patch
Patch2:		plasma-phone-components-dont-start-to-lockscreen.patch
# Revert the phone -> phoneshell rename until we have plasma 5.21
Patch3:		revert-1abb6737e4b26d2a0e056c51f0a5ed4194e47595.patch
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
BuildRequires:	pkgconfig(gstreamer-1.0)
Requires:	plasma-workspace
Requires:	plasma-nano
Requires:	qml(org.kde.plasma.core)
Requires:	qml(org.kde.plasma.components)
Requires:	qml(org.kde.plasma.workspace.components)
Requires:	qml(org.kde.plasma.networkmanagement)
Requires:	qml(org.kde.bluezqt)
Requires:	qml(org.kde.plasma.private.volume)
Requires:	qml(org.kde.notificationmanager)
Requires:	qml(org.kde.kirigami)
Requires:	qml(org.kde.taskmanager)
Requires:	qml(org.kde.plasma.private.nanoshell)
Requires:	qml(org.kde.plasma.private.mobileshell)
Requires:	qml(org.kde.plasma.private.containmentlayoutmanager)
Requires:	qml(org.kde.kquickcontrolsaddons)
Requires:	qml(org.kde.draganddrop)
Requires:	qml(org.kde.plasma.extras)
Requires:	qml(org.kde.milou)
Requires:	qml(QtGraphicalEffects)
Requires:	qt5-qtquickcontrols2
Requires:	kwin
Requires:	plasma-pa
Requires:	plasma-nm-mobile
# Used by the screenshot button
Requires:	spectacle

%description
Plasma components for mobile phones

%package wayland
Summary:	Wayland session files for Plasma phone components
Requires:	plasma-workspace-wayland

%description wayland
Wayland session files for Plasma phone components

%package x11
Summary:	X11 session files for Plasma phone components
Requires:	plasma-workspace-x11

%description x11
X11 session files for Plasma phone components

%prep
%if "%{?commit:%{commit}}" != ""
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-master
%endif
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
#%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%{_datadir}/kservices5/kwin-script-org.kde.phone.multitasking.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.activities.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.homescreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.krunner.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.panel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.taskpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/kwin/scripts/org.kde.phone.multitasking
%{_datadir}/metainfo/org.kde.phone.activities.appdata.xml
%{_datadir}/metainfo/org.kde.phone.krunner.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.activities
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.krunner
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%{_datadir}/knotifications5/plasma_phone_components.notifyrc
%{_datadir}/plasma/shells/org.kde.plasma.phone
#{_datadir}/plasma/shells/org.kde.plasma.phoneshell
#{_datadir}/kservices5/plasma-applet-org.kde.plasma.phoneshell.desktop
#{_datadir}/metainfo/org.kde.plasma.phoneshell.appdata.xml

%files wayland
%{_bindir}/kwinwrapper
%{_datadir}/wayland-sessions/plasma-mobile.desktop

%files x11
%{_bindir}/kwinwrapper_x11
%{_datadir}/xsessions/plasma-mobile-x11.desktop
