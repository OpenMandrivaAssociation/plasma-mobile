%define major	0
%define libname	%mklibname activeapp %{major}
%define devname	%mklibname -d activeapp %{major}

%define libnameN	%mklibname nepomukdatamodel %{major}

Name:		plasma-mobile
Summary:	KDE User Interface for mobile Devices
Version:	0.5
Release:	1
License:	GPL-2.0 or LGPL-2.0 or LGPL-2.1
Group:		Graphical desktop/KDE
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

%description
A touch enabled Plasma Active workspace aiming on different
(not only) mobile devices.

%package -n	%{devname}
Summary:	Developer files for %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	kdelibs4-devel

%description -n	%{devname}
%{summary}.

%package -n	%{libname}
Summary:	Runtime libraries for %{name}
%description -n %{libname}
%{summary}.

%package -n	%{libnameN}
Summary:	Runtime libraries for %{name}
%description -n %{libnameN}
%{summary}.

%package	mouse-cursor-themes
Summary:	Plasma Mobile mouse cursor themes
BuildArch:	noarch
%description	mouse-cursor-themes
%{summary}.

%package	wallpapers
Summary:	KDE Plasma Active wallpapers
Requires:	kde-filesystem
BuildArch:	noarch
%description	wallpapers
%{summary}.

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
#-DBUILD_HANDSET=False
%make

%install
%makeinstall_std -C build

%files
%doc LICENSE.GPL-2 LICENSE.LGPL-2 LICENSE.LGPL-2.1
%{_kde_bindir}/active-aboutapp
%{_kde_bindir}/active-filebrowser
%{_kde_bindir}/active-settings
%{_kde_bindir}/active-webbrowser
%{_kde_bindir}/plasma-device
%{_kde_bindir}/plasma-widgetstrip
%{_kde_libdir}/kde4/imports/org/kde/active/
%{_kde_libdir}/kde4/imports/org/kde/metadatamodels/
%{_kde_libdir}/kde4/imports/org/kde/plasma/mobilecomponents/
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/libkdeinit4_*.so
%{_kde_libdir}/kde4/libexec/activedatetimehelper
%{_kde_libdir}/kde4/libexec/active-integration-helper
%{_kde_libdir}/kde4/libexec/active-sshd-helper
%{_kde_libdir}/kconf_update_bin/activenotifications-to-orgkdenotifications
%{_kde_appsdir}/kconf_update/activenotifications-to-orgkdenotifications.upd

%{_kde_datadir}/applications/kde4/active-about.desktop
%{_kde_datadir}/applications/kde4/active-alarms.desktop
%{_kde_datadir}/applications/kde4/active-books.desktop
%{_kde_datadir}/applications/kde4/active-filebrowser.desktop
%{_kde_datadir}/applications/kde4/active-imageviewer.desktop
%{_kde_datadir}/applications/kde4/active-settings.desktop
%{_kde_datadir}/applications/kde4/active-web-browser.desktop
%{_kde_datadir}/applications/kde4/widget-strip.desktop
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_iconsdir}/oxygen/*/*/*
%{_kde_appsdir}/active-webbrowser/
%{_kde_appsdir}/desktoptheme/air-mobile/
%{_kde_appsdir}/desktoptheme/default/icons/*
%{_kde_appsdir}/desktoptheme/oxygen-mobile/
%{_kde_appsdir}/plasma/
%{_kde_appsdir}/plasma-widgetstrip/
%{_kde_appsdir}/solid/actions/browse-files.desktop
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_datadir}/dbus-1/system-services/org.kde.active.*
%{_datadir}/polkit-1/actions/org.kde.active.*
%{_sysconfdir}/dbus-1/system.d/org.kde.active.clockconfig.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.active.sshdcontrol.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.active.integration.conf

%files -n %{devname}
%{_kde_includedir}/*.h
%{_kde_libdir}/libactiveapp.so
%{_kde_libdir}/libnepomukdatamodel.so
%{_kde_appsdir}/cmake/modules/FindActiveApp.cmake
%{_libdir}/cmake/NepomukDataModel/*

%files -n %{libname}
%{_kde_libdir}/libactiveapp.so.%{major}*

%files -n %{libnameN}
%{_kde_libdir}/libnepomukdatamodel.so.%{major}*
%{_kde_libdir}/libnepomukdatamodel.so.1.*

%files mouse-cursor-themes
%{_kde_iconsdir}/plasmamobilemouse/

%files wallpapers
%{_kde_datadir}/wallpapers/HorosGreen/
