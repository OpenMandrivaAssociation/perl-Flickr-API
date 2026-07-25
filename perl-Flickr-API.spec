%define upstream_name    Flickr-API
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Perl interface to the flickr.com API 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/iamcal/perl-Flickr-API
Source0:	https://cpan.metacpan.org/authors/id/I/IA/IAMCAL/Flickr-API-%{upstream_version}.tar.gz

BuildRequires:	make
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
