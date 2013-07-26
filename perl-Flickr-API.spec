%define upstream_name    Flickr-API
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.08
Release:	1

Summary:	Perl interface to the flickr.com API 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/I/IA/IAMCAL/Flickr-API-1.08.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(XML::Parser::Lite::Tree)
BuildArch:	noarch

%description
Perl interface to the flickr.com API

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorlib}/
%{_mandir}/*/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 654191
- rebuild for updated spec-helper

* Wed Aug 26 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 421385
- update to 1.04

* Tue Aug 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 420894
- update to 1.03

* Wed Aug 05 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 410053
- update to 1.02

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.01-2mdv2009.1
+ Revision: 350225
- 2009.1 rebuild

* Thu Oct 02 2008 Pascal Terjan <pterjan@mandriva.org> 1.01-1mdv2009.0
+ Revision: 290801
- Update to 1.01 to support latest XML::Parser::Lite::Tree

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-3mdv2009.0
+ Revision: 257060
- rebuild

* Wed Feb 06 2008 Funda Wang <fwang@mandriva.org> 0.09-1mdv2008.1
+ Revision: 162939
- update to new version 0.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 11 2007 Pascal Terjan <pterjan@mandriva.org> 0.08-2mdv2008.0
+ Revision: 26369
- move make test to check section


* Mon Mar 20 2006 Pascal Terjan <pterjan@mandriva.org> 0.08-1mdk
- New release 0.08

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-3mdk
- fix BuildRequires

* Sat Sep 10 2005 Pascal Terjan <pterjan@mandriva.org> 0.07-2mdk
- Buildrequires perl-XML-Parser-Lite-Tree (for make test)

* Wed Aug 31 2005 Pascal Terjan <pterjan@mandriva.org> 0.07-1mdk
- First version of the package


