# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name LWP-Authen-Wsse

Summary: library for enabling X-WSSE authentication in LWP
Name: perl-LWP-Authen-Wsse
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LWP-Authen-Wsse/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/LWP-Authen-Wsse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is a library for enabling X-WSSE authentication in LWP.

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
%{perl_vendorlib}/LWP/Authen/Wsse.pm

%changelog
* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
