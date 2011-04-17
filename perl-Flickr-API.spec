%define upstream_name    Flickr-API
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl interface to the flickr.com API 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-XML-Parser-Lite-Tree
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl interface to the flickr.com API

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
