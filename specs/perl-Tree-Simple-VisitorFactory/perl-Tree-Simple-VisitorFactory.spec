# $Id$
# Authority: dries
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Simple-VisitorFactory

Summary: Visitor for Tree::Simple objects
Name: perl-Tree-Simple-VisitorFactory
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Simple-VisitorFactory/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STEVAN/Tree-Simple-VisitorFactory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements different versions of the Visitor pattern for Simple::Tree objects.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/Simple/VisitorFactory.pm
%{perl_vendorlib}/Tree/Simple/Visitor/

%changelog
* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
