%define name rox-musicbox
%define oname MusicBox
%define version 027
%define release %mkrel 7

Summary: Music player for the ROX desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.hayber.us/rox/musicbox/%{oname}-%{version}.tar.bz2
Patch: MusicBox-026-pic.patch
License: GPL
Group: Sound
URL: http://www.hayber.us/rox/MusicBox/
BuildRoot: %{_tmppath}/%{name}-buildroot
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




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 027-7mdv2011.0
+ Revision: 614715
- the mass rebuild of 2010.1 packages

* Fri Apr 02 2010 Funda Wang <fwang@mandriva.org> 027-6mdv2010.1
+ Revision: 530759
- rebuild

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 027-5mdv2010.0
+ Revision: 433395
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 027-4mdv2009.0
+ Revision: 260301
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 027-3mdv2009.0
+ Revision: 251406
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 027-1mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 027-1mdv2007.0
+ Revision: 111751
- Import rox-musicbox

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 027-1mdv2007.1
- disable flac
- new version

* Tue Aug 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 026-1mdv2007.0
- Rebuild

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 026-1mdk
- fix build on x86_64
- New release 026

* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 024-2mdk
- rebuild for allegro

* Tue Oct 18 2005 Götz Waschk <waschk@mandriva.org> 024-1mdk
- no more noarch
- fix URL
- update buildrequires
- New release 024

* Tue Oct 19 2004 Götz Waschk <waschk@linux-mandrake.com> 019-1mdk
- fix file list
- New release 019

* Wed May 19 2004 Götz Waschk <waschk@linux-mandrake.com> 017.1-2mdk
- fix URL

* Wed May 19 2004 Götz Waschk <waschk@linux-mandrake.com> 017.1-1mdk
- new version

* Thu Apr 15 2004 Götz Waschk <waschk@linux-mandrake.com> 015-1mdk
- initial package

