%define	modname	JSON-PP
%define	modver	2.27200

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	6

Summary:	Dummy module providing JSON::PP::Boolean
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/JSON/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module is the JSON::XS manpage compatible pure Perl module. (Perl 5.8
or later is recommended)

JSON::XS is the fastest and most proper JSON module on CPAN. It is written
by Marc Lehmann in C, so must be compiled and installed in the used
environment.

JSON::PP is a pure-Perl module and has compatibility to JSON::XS.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{perl_vendorlib}/*
%{_bindir}/json_pp
%{_mandir}/man3/*
%{_mandir}/man1/json_pp.1*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.272.0-3
- rebuild against new perl-5.16.2
- cleanups

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.272.0-1mdv2011.0
+ Revision: 682134
- update to new version 2.27200

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.271.50-2
+ Revision: 657443
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.271.50-1
+ Revision: 643397
- update to new version 2.27105

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.271.40-1
+ Revision: 635293
- import perl-JSON-PP

