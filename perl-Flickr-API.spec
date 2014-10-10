%define upstream_name    Flickr-API
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl interface to the flickr.com API 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{upstream_name}-%{upstream_version}.tar.gz

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
