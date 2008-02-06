%define name perl-Flickr-API
%define pkgname Flickr-API
%define version 0.09
%define release %mkrel 1

Summary:	Perl interface to the flickr.com API 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{pkgname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{pkgname}/
BuildRequires:  perl-XML-Parser-Lite-Tree
BuildRequires:  perl-libwww-perl
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl

%description
Perl interface to the flickr.com API

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{perl_vendorlib}/
%{_mandir}/*/*

