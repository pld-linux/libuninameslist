Summary:	Library with unicode character names list
Summary(pl):	Biblioteka z list± nazw znaków unicode
Name:		libuninameslist
Version:	030713
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libuninameslist/%{name}_src-%{version}.tgz
# Source0-md5:	051a0377d8e1674de9dc8da062b32646
URL:		http://libuninameslist.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library with unicode character names list.

%description -l pl
Biblioteka z list± nazw znaków unicode.

%package devel
Summary:	Header files for libuninameslist library
Summary(pl):	Pliki nag³ówkowe biblioteki libuninameslist
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libuninameslist library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libuninameslist.

%package static
Summary:	Static libuninameslist library
Summary(pl):	Statyczna biblioteka libuninameslist
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libuninameslist library.

%description static -l pl
Statyczna biblioteka libuninameslist.

%prep
%setup -q -n %{name}

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	incdir=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
