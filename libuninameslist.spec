#
# Conditional build:
%bcond_without	static_libs	# disable static libraries
#
Summary:	Library with unicode character names list
Summary(pl.UTF-8):	Biblioteka z listą nazw znaków unicode
Name:		libuninameslist
Version:	20091231
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libuninameslist/%{name}-%{version}.tar.bz2
# Source0-md5:	14f47d50fb0e05c5029298847437feab
URL:		http://libuninameslist.sourceforge.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library with unicode character names list.

%description -l pl.UTF-8
Biblioteka z listą nazw znaków unicode.

%package devel
Summary:	Header files for libuninameslist library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libuninameslist
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libuninameslist library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libuninameslist.

%package static
Summary:	Static libuninameslist library
Summary(pl.UTF-8):	Statyczna biblioteka libuninameslist
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
%attr(755,root,root) %{_libdir}/libuninameslist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuninameslist.so.0
%attr(755,root,root) %{_libdir}/libuninameslist-fr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuninameslist-fr.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuninameslist.so
%attr(755,root,root) %{_libdir}/libuninameslist-fr.so
%{_libdir}/libuninameslist.la
%{_libdir}/libuninameslist-fr.la
%{_includedir}/uninameslist.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libuninameslist.a
%{_libdir}/libuninameslist-fr.a
%endif
