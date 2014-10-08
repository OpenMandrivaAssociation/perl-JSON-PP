%define	modname	JSON-PP
%define modver 2.27203

Summary:	Dummy module providing JSON::PP::Boolean
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/JSON/JSON-PP-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
This module is the JSON::XS manpage compatible pure Perl module. (Perl 5.8
or later is recommended)

JSON::XS is the fastest and most proper JSON module on CPAN. It is written
by Marc Lehmann in C, so must be compiled and installed in the used
environment.

JSON::PP is a pure-Perl module and has compatibility to JSON::XS.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{perl_vendorlib}/*
%{_bindir}/json_pp
%{_mandir}/man3/*
%{_mandir}/man1/json_pp.1*


