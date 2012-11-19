Summary:	On-screen Input Pad to Send Characters with Mouse
Name:		input-pad
Version:	1.0.1
Release:	6
License:	LGPL v2+
Group:		Libraries
Source0:	http://input-pad.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	320461990a87fc31fd504c438fe9707a
Patch0:		%{name}-format-security.patch
URL:		http://code.google.com/p/input-pad/
BuildRequires:	eekboard-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	swig-python
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The input pad is a tool to send a character on button to text
applications.

%package devel
Summary:	Development tools for input-pad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The input-pad-devel package contains the header files.

%package -n python-input-pad
Summary:	Input Pad for python
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python-input-pad
The input-pad-python package contains the python wrapper files.

%package eek
Summary:	Input Pad with eekboard extension
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description eek
The input-pad-eek package contains eekboard extension module

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-gtk=3.0 \
	--enable-eek \
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/input-pad
%attr(755,root,root) %{_libdir}/libinput-pad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinput-pad.so.[0-9]
%dir %{_libdir}/%{name}-1.0
%dir %{_libdir}/%{name}-1.0/modules
%dir %{_libdir}/%{name}-1.0/modules/xkeysend
%dir %{_libdir}/%{name}-1.0/modules/kbdui
%attr(755,root,root) %{_libdir}/%{name}-1.0/modules/xkeysend/libinput-pad-xtest-gdk.so
%{_datadir}/%{name}
%{_pixmapsdir}/input-pad.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1.0
%attr(755,root,root) %{_libdir}/libinput-pad.so
%{_pkgconfigdir}/input-pad.pc

%files -n python-input-pad
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{name}-1.0
%attr(755,root,root) %{py_sitedir}/%{name}-1.0/*.so
%attr(755,root,root) %{py_sitedir}/%{name}-1.0/*.py*
%{py_sitedir}/pyinput_pad.pth

%files eek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-1.0/modules/kbdui/libinput-pad-eek-gtk.so
