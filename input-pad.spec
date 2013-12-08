Summary:	On-screen Input Pad to Send Characters with Mouse
Summary(pl.UTF-8):	Pole wprowadzania znaków na ekranie przy użyciu myszy
Name:		input-pad
Version:	1.0.3
Release:	2
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/input-pad/downloads/list
Source0:	http://input-pad.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	70f3d0273da97d576e80b4f45a112fec
URL:		http://code.google.com/p/input-pad/
BuildRequires:	eekboard-devel >= 1.0.6
BuildRequires:	glib2-devel >= 1:2.8
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	swig-python
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	glib2 >= 1:2.8
Requires:	gtk+3 >= 3.0
Requires:	libxklavier >= 4.0
Requires:	libxml2 >= 2.0
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
Requires:	glib2-devel >= 1:2.8
Requires:	gtk+3-devel >= 3.0
Requires:	libxklavier-devel >= 4.0
Requires:	libxml2-devel >= 2.0

%description devel
The input-pad-devel package contains the header files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki input-pad.

%package -n python-input-pad
Summary:	Input Pad for Python
Summary(pl.UTF-8):	Biblioteka Input Pad dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-input-pad
The input-pad-python package contains the Python wrapper files.

%description -n python-input-pad -l pl.UTF-8
Ten pakiet zawiera pliki obudowania Pythona dla biblioteki input-pad.

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
	--with-gtk=3.0 \
	--enable-eek \
	--enable-pygobject2 \
	--enable-xtest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-1.0/modules/xkeysend/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}-1.0/modules/kbdui/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{name}-1.0/*.la
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/input-pad
%attr(755,root,root) %{_libdir}/libinput-pad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinput-pad.so.1
%{_libdir}/girepository-1.0/InputPad-1.0.typelib
%dir %{_libdir}/%{name}-1.0
%dir %{_libdir}/%{name}-1.0/modules
%dir %{_libdir}/%{name}-1.0/modules/kbdui
%dir %{_libdir}/%{name}-1.0/modules/xkeysend
%attr(755,root,root) %{_libdir}/%{name}-1.0/modules/xkeysend/libinput-pad-xtest-gdk.so
%{_datadir}/%{name}
%{_pixmapsdir}/input-pad.png
%{_mandir}/man1/input-pad.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinput-pad.so
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/input-pad.pc
%{_datadir}/gir-1.0/InputPad-1.0.gir

%files -n python-input-pad
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{name}-1.0
%attr(755,root,root) %{py_sitedir}/%{name}-1.0/_input_pad*.so
%{py_sitedir}/%{name}-1.0/*.py[co]
%{py_sitedir}/pyinput_pad.pth

%files eek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-1.0/modules/kbdui/libinput-pad-eek-gtk.so
