#define snapshot 20210108
#define commit 6204b90a5106e1a8acb1853efa0c8555d7c3097c
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma-mobile
Version:	5.26.5
Summary:	Plasma components for mobile phones
# https://invent.kde.org/plasma/plasma-mobile
%if "%{?commit:%{commit}}" != ""
Source0:	https://invent.kde.org/plasma/plasma-mobile/-/archive/%{commit}/plasma-mobile-%{commit}.tar.bz2
Release:	1.%{snapshot}.%{commit}1
%else
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma/plasma-mobile/-/archive/master/plasma-mobile-master.tar.bz2
Release:	1.%{snapshot}1
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Release:	1
%endif
%endif
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
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
BuildRequires:	cmake(KWinDBusInterface)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(LibKWorkspace)
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
Obsoletes:	%{name}-wayland < %{EVRD}
Obsoletes:	%{name}-x11 < %{EVRD}

%description
Plasma components for mobile phones.

%prep
%if "%{?commit:%{commit}}" != ""
%autosetup -p1 -n plasma-mobile-%{commit}
%else
%if 0%{?snapshot}
%autosetup -p1 -n plasma-mobile-master
%else
%autosetup -p1 -n plasma-mobile-%{version}
%endif
%endif
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
#%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
%{_libdir}/qt5/qml/org/kde/plasma/mm
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%{_datadir}/knotifications5/plasma_phone_components.notifyrc
%{_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_datadir}/metainfo/org.kde.plasma.phoneshell.appdata.xml
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot
%{_datadir}/kpackage/kcms/kcm_mobileshell
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_bindir}/startplasmamobile
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen_halcyon.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_datadir}/applications/kcm_mobileshell.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/metainfo/org.kde.phone.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.phone.homescreen.halcyon.appdata.xml
%{_datadir}/metainfo/org.kde.phone.panel.appdata.xml
%{_datadir}/metainfo/org.kde.phone.taskpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.location.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record
