#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Library with unicode character names list
Summary(pl.UTF-8):	Biblioteka z listą nazw znaków unicode
Name:		libuninameslist
Version:	20230916
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/fontforge/libuninameslist/releases
Source0:	https://github.com/fontforge/libuninameslist/releases/download/%{version}/%{name}-dist-%{version}.tar.gz
# Source0-md5:	2dd15b7d0ab99dfdf8a6ece1eecf1cb9
URL:		http://libuninameslist.sourceforge.net/
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
%setup -q

%build
%configure \
	--enable-frenchlib \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libuninameslist*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README README.md
%attr(755,root,root) %{_libdir}/libuninameslist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuninameslist.so.1
%attr(755,root,root) %{_libdir}/libuninameslist-fr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuninameslist-fr.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuninameslist.so
%attr(755,root,root) %{_libdir}/libuninameslist-fr.so
%{_includedir}/uninameslist.h
%{_includedir}/uninameslist-fr.h
%{_pkgconfigdir}/libuninameslist.pc
%{_mandir}/man3/libuninameslist.3*
%{_mandir}/man3/libuninameslist-fr.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libuninameslist.a
%{_libdir}/libuninameslist-fr.a
%endif
