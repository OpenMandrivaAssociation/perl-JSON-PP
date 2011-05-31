%define upstream_name    JSON-PP
%define upstream_version 2.27200

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Dummy module providing JSON::PP::Boolean
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is the JSON::XS manpage compatible pure Perl module. (Perl 5.8
or later is recommended)

JSON::XS is the fastest and most proper JSON module on CPAN. It is written
by Marc Lehmann in C, so must be compiled and installed in the used
environment.

JSON::PP is a pure-Perl module and has compatibility to JSON::XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/json_pp
/usr/share/man/man1/json_pp.1.xz

