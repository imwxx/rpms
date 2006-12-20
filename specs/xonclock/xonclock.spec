# $Id$
# Authority: dries
# Upstream: 

%{?dist: %{expand: %%define %dist 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: On-screen analog clock
Name: xonclock
Version: 0.0.8.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://xonclock.sourceforge.net/

Source: http://dl.sf.net/xonclock/xonclock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtiff-devel, libjpeg-devel, libpng-devel
%{!?_without_modxorg:BuildRequires: freetype-devel, libX11-devel, libXext-devel, libXpm-devel, libXrender-devel, libXft-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Xonclock is a simple on-screen analog clock.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Xonclock
Comment=On-screen analog clock
Exec=xonclock
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure CFLAGS="-I/usr/include/freetype2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/xonclock*
%{_bindir}/xonclock
%{_datadir}/xonclock/
%{_datadir}/applications/*xonclock.desktop

%changelog
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.8.5-1
- Initial package.
