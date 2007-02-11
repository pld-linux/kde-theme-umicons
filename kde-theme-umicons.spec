#$Revision: 1.7 $, $Date: 2007-02-11 22:16:37 $

%define		_name	umicons

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	2.0
Release:	2
License:	Free for personal use
Group:		Themes
#Source0:	http://files.deviantart.com/icon/nixicons/Umicons_for_KDE.tar_2.gz
Source0:	http://easylinuxguide.com/downloads/kde-iconthemes/Umicons_for_KDE.tar_2.gz
# Source0-md5:	23e21986ee8402729f5934a3af1e041b
URL:		http://www.kde-look.org/content/show.php?content=7214
Requires:	kde-icons-%{_name}
Requires:	kde-wallpaper-%{_name}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	/usr/share/wallpapers

%description -n kde-wallpaper-%{_name}
A wallpaper to go with KDE %{_name} theme.

%description -n kde-wallpaper-%{_name} -l pl
Tapeta pasuj±ca do motywu %{_name}.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl):	Obrazki dla u¿ytkowników w KDM - %{_name}
Group:		Themes
Requires:	/usr/share/wallpapers

%description -n kdm-user-pictures-%{_name}
KDM user picture - %{_name}.

%description -n kdm-user-pictures-%{_name} -l pl
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

%files

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kdm-user-pictures-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/*
