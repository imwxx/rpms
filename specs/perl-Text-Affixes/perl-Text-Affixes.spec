# $Id$
# Authority: dries
# Upstream: Jos&#233; Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Affixes

Summary: Prefixes and suffixes analysis of text
Name: perl-Text-Affixes
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Affixes/

Source: http://search.cpan.org/CPAN/authors/id/C/CO/COG/Text-Affixes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Prefixes and suffixes analysis of text.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Affixes.pm
%{perl_vendorlib}/auto/Text/Affixes/

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
