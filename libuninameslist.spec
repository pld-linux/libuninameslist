#
# Conditional build:
%bcond_without	static_libs	# disable static libraries
#
Summary:	Library with unicode character names list
Summary(pl.UTF-8):   Biblioteka z listą nazw znaków unicode
Name:		libuninameslist
Version:	20060907
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libuninameslist/%{name}_src-%{version}.tgz
# Source0-md5:	e5090105b9f09e76838a0af3220b371d
URL:		http://libuninameslist.sourceforge.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library with unicode character names list.

%description -l pl.UTF-8
Biblioteka z listą nazw znaków unicode.

%package devel
Summary:	Header files for libuninameslist library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libuninameslist
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libuninameslist library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libuninameslist.

%package static
Summary:	Static libuninameslist library
Summary(pl.UTF-8):   Statyczna biblioteka libuninameslist
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libuninameslist library.

%description static -l pl.UTF-8
Statyczna biblioteka libuninameslist.

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.* .
%configure \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static

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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
