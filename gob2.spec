Summary:	GTK+ Object Builder
Name:		gob2
Version:	2.0.18
Release:	%mkrel 5
License:	GPLv2+
Group:		Development/GNOME and GTK+
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.5z.com/jirka/linux.html#gob
BuildRequires:	flex
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
GOB2 is a simple preprocessor for making GTK+ objects.  It makes objects
from a single file which has inline C code so that you don't have to edit
the generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README AUTHORS NEWS TODO ChangeLog
%doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*



%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.0.18-3mdv2011.0
+ Revision: 672447
- fix br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Jan 06 2011 Götz Waschk <waschk@mandriva.org> 2.0.18-1mdv2011.0
+ Revision: 629183
- update to new version 2.0.18

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.17-2mdv2011.0
+ Revision: 605490
- rebuild

* Fri Apr 02 2010 Götz Waschk <waschk@mandriva.org> 2.0.17-1mdv2010.1
+ Revision: 530794
- update to new version 2.0.17

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.16-2mdv2010.1
+ Revision: 522742
- rebuilt for 2010.1

* Tue Jul 21 2009 Götz Waschk <waschk@mandriva.org> 2.0.16-1mdv2010.0
+ Revision: 398434
- new version
- drop patch

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 2.0.15-2mdv2009.1
+ Revision: 364958
- fix str fmt

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.15-2mdv2009.0
+ Revision: 221096
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 21 2007 Götz Waschk <waschk@mandriva.org> 2.0.15-1mdv2008.1
+ Revision: 110868
- new version

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.0.14-3mdv2008.0
+ Revision: 91342
- rebuild for 2008
- don't package COPYING
- new license policy
- minor spec clean


* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.14-2mdv2007.0
+ Revision: 108670
- Import gob2

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.14-2mdv2007.1
- Rebuild

* Fri Jan 06 2006 Götz Waschk <waschk@mandriva.org> 2.0.14-1mdk
- New release 2.0.14

* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdk
- New release 2.0.13
- use mkrel

* Tue Jul 26 2005 G�tz Waschk <waschk@mandriva.org> 2.0.12-1mdk
- New release 2.0.12

* Thu Oct 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.11-1mdk
- New release 2.0.11

* Wed Jul 21 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.0.9-1mdk
- fix source URL
- New release 2.0.9

* Thu Jun 24 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.8-1mdk
- New release 2.0.8

* Wed Apr 07 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.0.7-1mdk
- new version

