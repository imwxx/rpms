# $Id$
# Authority: dries
# Upstream: Gene Boggs <gene$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Counting

Summary: Combinatorial counting operations
Name: perl-Math-Counting
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Counting/

Source: http://search.cpan.org/CPAN/authors/id/G/GE/GENE/Math-Counting-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for combinatorial counting operations.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Counting.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
