Summary:	On-screen Input Pad to Send Characters with Mouse
Summary(pl.UTF-8):	Pole wprowadzania znaków na ekranie przy użyciu myszy
Name:		input-pad
Version:	1.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/fujiwarat/input-pad/releases
Source0:	https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aa4684c08bc8b5c7f91b22bd3885a3cd
URL:		https://github.com/fujiwarat/input-pad
BuildRequires:	eekboard-devel >= 1.0.6
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.37
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	glib2 >= 1:2.37
Requires:	gtk+3 >= 3.12
Requires:	libxklavier >= 4.0
Requires:	libxml2 >= 2.0
Obsoletes:	python-input-pad < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The input pad is a tool to send a character on button to text
applications.

%description -l pl.UTF-8
Input Pad to narzędzie pozwalające na wysyłanie znaków do aplikacji
tekstowych przyciskiem myszy.

%package devel
Summary:	Development files for input-pad
Summary(pl.UTF-8):	Pliki programistyczne biblioteki input-pad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.37
Requires:	gtk+3-devel >= 3.12
Requires:	libxklavier-devel >= 4.0
Requires:	libxml2-devel >= 2.0

%description devel
The input-pad-devel package contains the header files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki input-pad.

%package eek
Summary:	Input Pad with eekboard extension
Summary(pl.UTF-8):	Rozszerzenie eekboard dla biblioteki input-pad
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description eek
The input-pad-eek package contains eekboard extension module.

%description eek -l pl.UTF-8
Ten pakiet zawiera moduł rozszerzenia eekboard dla biblioteki
input-pad.

%prep
%setup -q

%build
%configure \
	--enable-eek \
	--enable-xtest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-1.1/modules/xkeysend/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-1.1/modules/kbdui/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/input-pad
%attr(755,root,root) %{_libdir}/libinput-pad-1.0.so.*.*.*
%ghost %{_libdir}/libinput-pad-1.0.so.1
%{_libdir}/girepository-1.0/InputPad-1.1.typelib
%dir %{_libdir}/%{name}-1.1
%dir %{_libdir}/%{name}-1.1/modules
%dir %{_libdir}/%{name}-1.1/modules/kbdui
%dir %{_libdir}/%{name}-1.1/modules/xkeysend
%attr(755,root,root) %{_libdir}/%{name}-1.1/modules/xkeysend/libinput-pad-xtest-gdk.so
%{_datadir}/%{name}
%{_pixmapsdir}/input-pad.png
%{_mandir}/man1/input-pad.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libinput-pad-1.0.so
%{_includedir}/input-pad-1.1
%{_pkgconfigdir}/input-pad.pc
%{_datadir}/gir-1.0/InputPad-1.1.gir

%files eek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-1.1/modules/kbdui/libinput-pad-eek-gtk.so
