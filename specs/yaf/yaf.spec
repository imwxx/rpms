# $Id$
# Authority: dag

Summary: Yet Another Flow sensor
Name: yaf
Version: 2.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tools.netsa.cert.org/yaf/

Source: http://tools.netsa.cert.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
BuildRequires: libfixbuf-devel >= 1.0.0
BuildRequires: libpcap-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: pcre-devel
BuildRequires: pkgconfig

%description
YAF is Yet Another Flow sensor. It processes packet data from pcap(3) dumpfiles
as generated by tcpdump(1) or via live capture from an interface using pcap(3)
or an Endace DAG card into bidirectional flows, then exports those flows to
IPFIX Collecting Processes or in an IPFIX-based file format. YAF's output can
be used with the NetSA Aggregated Flow (NAF) toolchain.

%package devel
Summary: Static libraries and C header files for yaf
Group: Development
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig >= 0.8

%description devel
Static libraries and C header files for yaf.

%prep
%setup

%build

%configure \
    --disable-static \
    --enable-applabel

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/html/
%doc %{_mandir}/man1/airdaemon.1*
%doc %{_mandir}/man1/applabel.1*
%doc %{_mandir}/man1/filedaemon.1*
%doc %{_mandir}/man1/yaf.1*
%doc %{_mandir}/man1/yafdpi.1*
%doc %{_mandir}/man1/yafscii.1*
%config(noreplace) %{_sysconfdir}/yafApplabelRules.conf
%{_bindir}/airdaemon
%{_bindir}/filedaemon
%{_bindir}/yaf
%{_bindir}/yafcollect
%{_bindir}/yafscii
%{_libdir}/*.so*
%exclude %{_libdir}/libltdl.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.la
%exclude %{_includedir}/libltdl/
%exclude %{_includedir}/ltdl.h

%changelog
* Sun Aug 14 2011 Yury V. Zaytsev <yury@shurup.com> - 2.1.1-1
- Excluded libltdl, since yaf should get linked to the system one.
- Updated to release 2.1.1.

* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
