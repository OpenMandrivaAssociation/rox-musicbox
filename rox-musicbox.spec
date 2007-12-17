%define name rox-musicbox
%define oname MusicBox
%define version 027
%define release %mkrel 1

Summary: Music player for the ROX desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.hayber.us/rox/musicbox/%{oname}-%{version}.tar.bz2
Patch: MusicBox-026-pic.patch
License: GPL
Group: Sound
URL: http://www.hayber.us/rox/MusicBox/
Requires: rox-lib >= 1.9.8
Requires: pyvorbis
Requires: pyao
Requires: pymad
Requires: pyid3lib
#BuildRequires: libflac-devel
BuildRequires: python-devel
BuildRequires: swig

%description
MusicBox plays your mp3 and ogg files (yea!).  It supports ogg via
pyogg/libvorbis and mp3 via pymad/libmad.

MusicBox supports mp3, ogg files, directories, .pls and .m3u files to
build the playlist.  Any and all of these can be used together.

%prep
%setup -q -n %oname
%patch -p1
find  . -name .svn|xargs rm -rf

%build
#cd plugins/flac
#%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
mkdir -p %buildroot/%_libdir/apps
cp -r ../%oname %buildroot/%_libdir/apps/
rm -f %buildroot/%_libdir/apps/%oname/Messages/*.po
rm -f %buildroot/%_libdir/apps/%oname/messages.pot
# wrong bytecode version
rm -f %buildroot/%_libdir/apps/%oname/*.pyc
rm -f %buildroot/%_libdir/apps/%oname/Messages/dist
rm -f %buildroot/%_libdir/apps/%oname/Messages/update-po
rm -f %buildroot/%_libdir/apps/%oname/Messages/make_tips
#flac source code
rm -f %buildroot%_libdir/apps/%oname/plugins/flac/*.i
rm -f %buildroot%_libdir/apps/%oname/plugins/flac/*.c 
rm -f %buildroot%_libdir/apps/%oname/plugins/flac/Makefile

for gmo in %buildroot%_libdir/apps/%oname/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc %_libdir/apps/%oname/Help
%dir %_libdir/apps/%oname/
%dir %_libdir/apps/%oname/Messages
%_libdir/apps/%oname/Messages/tips.py
%_libdir/apps/%oname/plugins/
%_libdir/apps/%oname/Extras/
%_libdir/apps/%oname/images/
%_libdir/apps/%oname/AppRun
%_libdir/apps/%oname/.DirIcon
%_libdir/apps/%oname/*.py
%_libdir/apps/%oname/AppInfo.xml
%_libdir/apps/%oname/Options.xml
%_libdir/apps/%oname/tips


