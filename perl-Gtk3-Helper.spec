%define upstream_name	 Gtk3-Helper
%define	upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Perl helper module for Gtk3
License:    LGPLv2+ or Artistic
Group:      Development/GNOME and GTK+
Url:        https://metacpan.org/pod/Gtk3::Helper
Source0:    https://cpan.metacpan.org/authors/id/T/TV/TVIGNAUD/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Gtk3)
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Depends >= 0.300
%description
This module provides an helper for Gtk3.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build OPTIMIZE="%{optflags}"

%install
%make_install

%files
%doc COPYING Changes META.json META.yml README
%{perl_vendorlib}/Gtk3/Helper*
%_mandir/*/*
