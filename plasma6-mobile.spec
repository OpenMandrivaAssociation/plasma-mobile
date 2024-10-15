%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		plasma6-mobile
Version:	6.2.1
Summary:	Plasma components for mobile phones
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-mobile/-/archive/%{gitbranch}/plasma-mobile-%{gitbranchd}.tar.bz2#/plasma-mobile-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-mobile-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}1
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
#BuildRequires:	cmake(KF6Akonadi)
#BuildRequires:	cmake(KF6Libkdepim)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KWayland)
BuildRequires:	cmake(Wayland) >= 5.90.0
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick) >= 5.90.0
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6Baloo)
BuildRequires:	cmake(KF6Screen)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(LibKWorkspace)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KWin)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(libudev)
# For DBus interfaces
BuildRequires:	plasma6-kwin
Requires:	plasma6-workspace
Requires:	plasma6-nano
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
Requires:	plasma6-kwin
Requires:	plasma6-pa
# Used by the screenshot button
# (but only once ported to Plasma6)
#Requires:	spectacle
Obsoletes:	%{name}-wayland < %{EVRD}
Obsoletes:	%{name}-x11 < %{EVRD}

%description
Plasma components for mobile phones.

%prep
%autosetup -p1 -n plasma-mobile-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_bindir}/plasma-mobile-envmanager
%{_bindir}/plasma-mobile-initial-start
%{_bindir}/startplasmamobile
%{_qtdir}/plugins/kf6/kded/kded_plasma_mobile_start.so
%{_qtdir}/plugins/kwin/effects/plugins/mobiletaskswitcher.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.folio.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.halcyon.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.mobile.panel.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.mobile.taskpanel.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_info.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_onscreenkeyboard.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_power.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_time.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_qtdir}/qml/org/kde/plasma/mm
%{_qtdir}/qml/org/kde/plasma/mobileinitialstart
%{_qtdir}/qml/org/kde/plasma/private/mobileshell
%dir %{_qtdir}/qml/org/kde/plasma/quicksetting
%{_qtdir}/qml/org/kde/plasma/quicksetting/flashlight
%{_qtdir}/qml/org/kde/plasma/quicksetting/nightcolor
%{_qtdir}/qml/org/kde/plasma/quicksetting/powermenu
%{_qtdir}/qml/org/kde/plasma/quicksetting/record
%{_qtdir}/qml/org/kde/plasma/quicksetting/screenrotation
%{_qtdir}/qml/org/kde/plasma/quicksetting/screenshot
%dir %{_qtdir}/qml/org/kde/private/mobile/homescreen
%{_qtdir}/qml/org/kde/private/mobile/homescreen/halcyon
%{_datadir}/applications/kcm_cellular_network.desktop
%{_datadir}/applications/kcm_mobile_hotspot.desktop
%{_datadir}/applications/kcm_mobile_info.desktop
%{_datadir}/applications/kcm_mobile_onscreenkeyboard.desktop
%{_datadir}/applications/kcm_mobile_power.desktop
%{_datadir}/applications/kcm_mobile_time.desktop
%{_datadir}/applications/kcm_mobile_wifi.desktop
%{_datadir}/applications/kcm_mobileshell.desktop
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml
%{_datadir}/kwin/effects/mobiletaskswitcher
%{_datadir}/kwin/scripts/convergentwindows
%{_datadir}/metainfo/org.kde.breeze.mobile.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.homescreen.folio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.homescreen.halcyon.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.panel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.taskpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.*.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileshell.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultNavigationPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultStatusBar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.hotspot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksettings.*.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile
%dir %{_datadir}/plasma/mobileinitialstart
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.*
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel
%{_datadir}/plasma/quicksettings/*
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell
%{_qtdir}/plugins/kf6/kded/kded_plasma_mobile_autodetect_apn.so
%{_datadir}/plasma-mobile-apn-info
%{_bindir}/plasma-mobile-notificationtest
%{_datadir}/knotifications6/plasma_mobile_*.notifyrc
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar
