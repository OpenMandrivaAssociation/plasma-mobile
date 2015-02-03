Name:		plasma-mobile
Summary:	KDE User Interface for mobile Devices
Version:	0.5
Release:	1
License:	GPL-2.0 or LGPL-2.0 or LGPL-2.1
Group:		System/GUI/KDE
Url:		http://plasma-active.org/
Source0:	%{name}-%{version}.tar.xz
Source1:	plasma-device.desktop
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	cmake(KdepimLibs)
BuildRequires:	kdelibs4-devel
BuildRequires:	task-kde4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	oxygen-icon-theme
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
BuildRequires:	knetworkmanager-devel
Patch0:		kubuntu_no_dirmodel.diff
Patch1:		kubuntu_no_contourd.diff
Requires: kwin
Requires: startactive = 0.4
Requires: plasma-mobile-config = 0.4
Requires: kde-artwork-active = 0.4
Requires: share-like-connect = 0.4
Requires: plasmoid-networkmanagement

# Require all subpackages
# (except libraries, rpm wants to do that itself)
Requires: plasma-mobile-applets
Requires: plasma-mobile-applications
Requires: plasma-mobile-widgetstrip-shell
Requires: plasma-mobile-artwork
Suggests: plasma-mobile-mouse
Requires: plasma-mobile-components
Requires: plasma-mobile-containments
Requires: plasma-mobile-contourd
Requires: plasma-mobile-dataengines
Requires: plasma-mobile-qmlpackages
Requires: plasma-mobile-appsrunner
Requires: plasma-mobile-shell
Requires: plasma-mobile-wallpaperplugin


%description
This is a Plasma Desktop made for mobile devices such as smartphones and tablets.

%package applets
Summary: Todo
Group: System/GUI/KDE
%description applets
Todo.

%package applications
Summary: Todo
Group: System/GUI/KDE
%description applications
Todo.

# applications/common
%package -n libactiveapp0
Summary: Todo
Group: Development/Libraries/C and C++
%description -n  libactiveapp0
Todo.

%package -n libactiveapp-devel
Summary: Todo
Group: Development/Libraries/C and C++
Requires: libactiveapp0 = %{version}
%description -n  libactiveapp-devel
Todo.

# applications/widgetstrip
%package widgetstrip-shell
Summary: Todo
Group: System/GUI/KDE
%description widgetstrip-shell
Todo.

%package artwork
Summary: Todo
Group: System/GUI/KDE
%description artwork
Todo.

# artwork/mousetheme
%package mouse
Summary: Invisible mouse cursor for Plasma Active
Group: System/X11/Icons
%description mouse
Provides the invisible X11 cursor theme from the Plasma Active Project.

%package components
Summary: Todo
Group: System/GUI/KDE
%description components
Todo.

%package -n libnepomukdatamodel0
Summary: Todo
Group: Development/Libraries/C and C++
%description -n  libnepomukdatamodel0
Todo.

%package -n libnepomukdatamodel-devel
Summary: Todo
Group: Development/Libraries/C and C++
Requires: libnepomukdatamodel0 = %{version}
%description -n  libnepomukdatamodel-devel
Todo.

%package containments
Summary: Todo
Group: System/GUI/KDE
%description containments
Todo.

%package contourd
Summary: Todo
Group: System/GUI/KDE
%description contourd
Todo.

%package dataengines
Summary: Todo
Group: System/GUI/KDE
%description dataengines
Todo.

# handset

%package qmlpackages
Summary: Todo
Group: System/GUI/KDE
%description qmlpackages
Todo.

%package appsrunner
Summary: Todo
Group: System/GUI/KDE
%description appsrunner
Todo.

%package shell
Summary: Todo
Group: System/GUI/KDE
%description shell
Todo.

%package wallpaperplugin
Summary: Todo
Group: System/GUI/KDE
%description wallpaperplugin
Todo.

%prep
%setup -q
%apply_patches

%build
%cmake_kde4 -DBUILD_HANDSET=False
%make

%install
%makeinstall_std -C build

%files
%doc LICENSE.*

%files applets
%{_kde_applicationsdir}/active-alarms.desktop
%{_kde_services}/plasma-applet-org.kde.active.alarms.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.active.alarms
%{_kde_iconsdir}/*/*/apps/kalarm-active.*
%{_kde_services}/plasma-applet-org.kde.digital-clock.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.digital-clock
%{_kde_services}/plasma-applet-org.kde.locationchooser.desktop
%{_kde_services}/plasma-applet-locationchooser.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.locationchooser
%{_kde_libdir}/kde4/plasma_applet_locationchooser.so
%{_kde_iconsdir}/*/*/apps/plasmaapplet-location.*
%{_kde_iconsdir}/*/*/apps/plasmaapplet-location-changed.*
%{_kde_iconsdir}/*/*/apps/plasmaapplet-location-unknown.*
%{_kde_appsdir}/desktoptheme/default/icons/location*.svgz
# powerbutton
%{_kde_services}/plasma-applet-org.kde.active.powerbutton.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.active.powerbutton
# resourcelist
%{_kde_services}/plasma-applet-org.kde.resourcelist.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.resourcelist

%files applications
# about
%{_kde_bindir}/active-aboutapp
%{_kde_applicationsdir}/active-about.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.aboutapp
%{_kde_iconsdir}/*/*/apps/active-about.*
# common!!!!!!!!!!!
# filebrowser
%{_kde_bindir}/active-filebrowser
%{_kde_applicationsdir}/active-books.desktop
%{_kde_appsdir}/solid/actions/browse-files.desktop
%{_kde_applicationsdir}/active-filebrowser.desktop
%{_kde_applicationsdir}/active-imageviewer.desktop
%{_kde_services}/org.kde.active.imageviewerpart.desktop
%{_kde4_servicetypesdir}/plasma-filebrowserpart.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.filebrowser
%{_kde_appsdir}/plasma/packages/org.kde.active.imageviewerpart
%{_kde_appsdir}/plasma/packages/org.kde.active.audiopart
%{_kde_services}/org.kde.active.audiopart.desktop
%{_kde_iconsdir}/*/*/apps/active-image-viewer.*
%{_kde_iconsdir}/*/*/mimetypes/application-epub+zip.png
# settings
%{_kde4_servicetypesdir}/active-settingsmodule.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.settings
%{_kde_applicationsdir}/active-settings.desktop
%{_kde_bindir}/active-settings
# developmentmodule
%{_kde_libdir}/kde4/active_settings_devel.so
%{_kde_appsdir}/plasma/packages/org.kde.active.settings.development
%{_kde_services}/org.kde.active.settings.development.desktop
%{_libdir}/libexec/kde4/active-sshd-helper
%{_libdir}/libexec/kde4/active-integration-helper
%{_sysconfdir}/dbus-1/system.d/org.kde.active.integration.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.active.sshdcontrol.conf
%{_kde_datadir}/dbus-1/system-services/org.kde.active.integration.service
%{_kde_datadir}/dbus-1/system-services/org.kde.active.sshdcontrol.service
%{_kde_datadir}/polkit-1/actions/org.kde.active.integration.policy
%{_kde_datadir}/polkit-1/actions/org.kde.active.sshdcontrol.policy
# timemodule
%{_kde_libdir}/kde4/active_settings_time.so
%{_kde_appsdir}/plasma/packages/org.kde.active.settings.time
%{_kde_services}/org.kde.active.settings.time.desktop
%{_libdir}/libexec/kde4/activedatetimehelper
%{_sysconfdir}/dbus-1/system.d/org.kde.active.clockconfig.conf
%{_kde_datadir}/dbus-1/system-services/org.kde.active.clockconfig.service
%{_kde_datadir}/polkit-1/actions/org.kde.active.clockconfig.policy
# webmodule
%{_kde_appsdir}/plasma/packages/org.kde.active.settings.web
%{_kde_services}/org.kde.active.settings.web.desktop
# powermanagementmodule
%{_kde_appsdir}/plasma/packages/org.kde.active.settings.powermanagement
%{_kde_services}/org.kde.active.settings.powermanagement.desktop
# webbrowser
%{_kde_bindir}/active-webbrowser
%{_kde_applicationsdir}/active-web-browser.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.webbrowser
%{_kde_appsdir}/active-webbrowser
%{_kde_iconsdir}/*/*/apps/active-web-browser.*
# widgetstrip
# TODO: integrate into  or split applications package
%files widgetstrip-shell
%{_kde_bindir}/plasma-widgetstrip
%{_kde_libdir}/libkdeinit4_plasma-widgetstrip.so
%{_kde_applicationsdir}/widget-strip.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.widgetsexplorer
%{_kde_appsdir}/plasma-widgetstrip
%{_kde_iconsdir}/*/*/actions/dashboard-show.png
%{_kde_applicationsdir}/widget-strip.desktop
%{_kde_appsdir}/plasma/packages/org.kde.active.widgetsexplorer
# applications/common

# TODO: same thing for libactiveapp
%files -n libactiveapp0
%{_kde_libdir}/libactiveapp.so.0
%{_kde_libdir}/libactiveapp.so.0.1

%files -n libactiveapp-devel
%{_kde_includedir}/activeapp_export.h
%{_kde_includedir}/kdeclarativemainwindow.h
%{_kde_includedir}/kdeclarativeview.h
%{_kde_libdir}/libactiveapp.so
%{_kde_appsdir}/cmake/modules/FindActiveApp.cmake

%files artwork
# air-mobile
%{_kde_appsdir}/desktoptheme/air-mobile
# oxygen-mobile
%{_kde_appsdir}/desktoptheme/oxygen-mobile
# wallpapers; maybe separate subpackage?
%{_kde4_wallpapersdir}/HorosGreen

# artwork/mousetheme
%files mouse
%{_kde_iconsdir}/plasmamobilemouse

%files components
# dirmodel
%{_kde_libdir}/kde4/imports/org/kde/dirmodel
# metadatamodel
%{_kde_libdir}/kde4/imports/org/kde/metadatamodels
# mobilecomponents
%{_kde_libdir}/kde4/imports/org/kde/plasma/mobilecomponents
%{_kde_appsdir}/plasma/resourcedelegates
# settings
%dir %{_kde_libdir}/kde4/imports/org/kde/active
%{_kde_libdir}/kde4/imports/org/kde/active/settings

# components/metadatamodel/library
%files -n libnepomukdatamodel0
%{_kde_libdir}/libnepomukdatamodel.so.1.0
%{_kde_libdir}/libnepomukdatamodel.so.0

%files -n libnepomukdatamodel-devel
%{_kde_libdir}/libnepomukdatamodel.so
%{_kde_includedir}/nepomukdatamodel_export.h
%{_kde_includedir}/metadatamodel.h
%{_kde_includedir}/abstractqueryprovider.h
%{_kde_includedir}/basicqueryprovider.h
%{_kde_includedir}/timelinequeryprovider.h
%{_kde_includedir}/cloudqueryprovider.h
%{_kde_includedir}/resourcequeryprovider.h
%dir %{_kde_libdir}/cmake/NepomukDataModel
%{_kde_libdir}/cmake/NepomukDataModel/NepomukDataModelConfig.cmake
%{_kde_libdir}/cmake/NepomukDataModel/NepomukDataModelConfigVersion.cmake
%{_kde_libdir}/cmake/NepomukDataModel/NepomukDataModelLibraryTargets-release.cmake
%{_kde_libdir}/cmake/NepomukDataModel/NepomukDataModelLibraryTargets.cmake

%files containments
# activityscreen
%{_kde_services}/plasma-applet-org.kde.active.activityscreen.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.active.activityscreen
# appletstrip
%{_kde_services}/plasma-applet-org.kde.appletstrip.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.appletstrip
# webdashboard
%{_kde_services}/plasma-applet-org.kde.webdashboard.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.webdashboard
# systemtray
%{_kde_services}/plasma-applet-org.kde.active.systemtray.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.active.systemtray

%files contourd
%{_kde4_servicetypesdir}/contour-recommendationengine.desktop
%{_kde4_servicetypesdir}/contour-recommendationengine-qtscript.desktop
/usr/share/autostart/contour.desktop
%{_kde_bindir}/contour
%dir %{_kde_appsdir}/contour
%dir %{_kde_appsdir}/contour/scripts
# documentsplugin
%{_kde_services}/contour-recommendationengine-documents.desktop
%{_kde_libdir}/kde4/contour_recommendationengine_documents.so
# linksplugin
%{_kde_appsdir}/contour/scripts/org.kde.contour.links
%{_kde_services}/contour-recommendationengine-links.desktop
# mediapauseplugin
%{_kde_appsdir}/contour/scripts/org.kde.contour.mediapause
%{_kde_services}/contour-recommendationengine-mediapause.desktop

%files dataengines
%defattr(-,root,root)
# alarms
%{_kde_services}/plasma-engine-alarms.desktop
%{_kde_appsdir}/plasma/services/org.kde.alarms.operations
%{_kde_libdir}/kde4/plasma_engine_alarms.so
# apps
%{_kde_services}/plasma-dataengine-org.kde.active.apps.desktop
%{_kde_appsdir}/plasma/services/org.kde.active.apps.operations
%{_kde_libdir}/kde4/plasma_engine_active_apps.so
# devicecapabilities
%{_kde_services}/plasma-engine-devicecapabilities.desktop
%{_kde_libdir}/kde4/plasma_engine_devicecapabilities.so
# metadata
%{_kde_services}/plasma-engine-active-metadata.desktop
%{_kde_appsdir}/plasma/services/metadataservice.operations
%{_kde_libdir}/kde4/plasma_engine_active_metadata.so
# preview
%{_kde_services}/plasma-engine-preview.desktop
%{_kde_libdir}/kde4/plasma_engine_preview.so
# recommendations
%{_kde_libdir}/kde4/plasma_engine_recommendations.so
%{_kde_services}/plasma-dataengine-recommendations.desktop
%{_kde_appsdir}/plasma/services/recommendations.operations

%files qmlpackages
# activityswitcher
%{_kde_appsdir}/plasma/packages/org.kde.activityswitcher
# contour-tablet-homescreen
%{_kde_appsdir}/plasma/packages/org.kde.active.contour-tablet-homescreen
# recommendations
%{_kde_appsdir}/plasma/packages/org.kde.contour.recommendations
# launcher
%{_kde_appsdir}/plasma/packages/org.kde.active.launcher

%files appsrunner
%{_kde_services}/plasma-runner-org.kde.active.apps.desktop
%{_kde_libdir}/kde4/krunner_activeapps.so

%files shell
%{_kde_libdir}/libkdeinit4_plasma-device.so
%{_kde_bindir}/plasma-device
%{_kde_appsdir}/plasma/packages/org.kde.active.addresources
%{_kde_appsdir}/plasma/packages/org.kde.active.activityconfiguration
%{_kde_datadir}/xsessions/plasma-device.desktop
%{_kde_libdir}/kconf_update_bin/activenotifications-to-orgkdenotifications
%{_kde_appsdir}/kconf_update/activenotifications-to-orgkdenotifications.upd

%files wallpaperplugin
%{_kde_services}/plasma-wallpaper-mobileimage.desktop
%{_kde_libdir}/kde4/plasma_wallpaper_mobileimage.so
