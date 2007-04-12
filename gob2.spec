Summary: GOB2, The GTK+2 Object Builder
Name: gob2
Version: 2.0.14
Release: %mkrel 2
License: GPL
Group: Development/GNOME and GTK+
Source: http://ftp.gnome.org/pub/GNOME/sources/gob2/%{name}-%{version}.tar.bz2
Url: http://www.5z.com/jirka/linux.html#gob
BuildRequires: flex libglib2.0-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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

%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc examples

%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*


