#$Revision: 1.3 $, $Date: 2004-04-17 13:54:01 $

%define		_name	umicons

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	2.0
Release:	1
License:	Free for personal use
Group:		Themes
Source0:	http://files.deviantart.com/icon/nixicons/Umicons_for_KDE.tar_2.gz
# Source0-md5:
URL:		http://www.kde-look.org/content/show.php?content=7214
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
%{_name} is a new concept of icons.

%description -l pl
%{_name} to nowa koncepcja podej¶cia do ikon.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl):	Motyw ikon do kde - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
%{_name} is a new concept of icons.

%description -n kde-icons-%{_name} -l pl
%{_name} to nowa koncepcja podej¶cia do ikon.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl):	Tapeta do KDE - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
A wallpaper to go with KDE %{_name} theme.

%description -n kde-wallpaper-%{_name} -l pl
Tapeta pasuj±ca do motywu %{_name}.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl):	Obrazki dla u¿ytkowników w KDM - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdm

%description -n kdm-user-pictures-%{_name}
KDM user picture - %{_name}.

%description -n kdm-user-pictures-%{_name} -lpl
Obrazki dla u¿ytkowników w KDM - %{_name}.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/{wallpapers,apps/kdm/pics/users}
%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

cd $RPM_BUILD_ROOT%{_iconsdir}/Umicons_2.0
mv wallpaper/* $RPM_BUILD_ROOT%{_datadir}/wallpapers
mv kdm/* $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/
rm -rf wallpaper kdm
%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kdm-user-pictures-%{_name}
%{_datadir}/apps/kdm/pics/users/*
