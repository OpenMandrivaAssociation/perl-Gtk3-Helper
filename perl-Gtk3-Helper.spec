%define upstream_name	 Gtk3-Helper
%define	upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Perl helper module for Gtk3
License:    LGPLv2+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Gtk3)
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Depends >= 0.300
%description
This module provides an helper for Gtk3.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc COPYING Changes META.json META.yml MYMETA.yml README
%{perl_vendorlib}/Gtk3/Helper*
%_mandir/*/*
