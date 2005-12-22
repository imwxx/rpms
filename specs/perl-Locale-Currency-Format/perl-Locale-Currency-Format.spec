# $Id$
# Authority: dries
# Upstream: Tan D Nguyen <tnguyen$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Currency-Format

Summary: Functions for formatting monetary values
Name: perl-Locale-Currency-Format
Version: 1.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Currency-Format/

Source: http://search.cpan.org/CPAN/authors/id/T/TN/TNGUYEN/Locale-Currency-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl functions for formatting monetary values.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Locale/Currency/Format.pm

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
