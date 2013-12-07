%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GTK+ Object Builder
Name:		gob2
Version:	2.0.19
Release:	3
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		http://www.5z.com/jirka/linux.html#gob
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	flex
BuildRequires:	pkgconfig(glib-2.0)

%description
GOB2 is a simple preprocessor for making GTK+ objects.  It makes objects
from a single file which has inline C code so that you don't have to edit
the generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc README AUTHORS NEWS TODO ChangeLog
%doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*

