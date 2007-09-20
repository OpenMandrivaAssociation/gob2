Summary:	GTK+ Object Builder
Name:		gob2
Version:	2.0.14
Release:	%mkrel 3
License:	GPLv2+
Group:		Development/GNOME and GTK+
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.5z.com/jirka/linux.html#gob
BuildRequires:	flex
BuildRequires:	libglib2.0-devel
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

