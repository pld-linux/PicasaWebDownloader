Summary:	PicasaWeb Downloader
Summary(pl.UTF-8):	Narzędzie do ściągania albumów z serwisu PicasaWeb
Name:		PicasaWebDownloader
Version:	1.2
Release:	1
License:	WTFPL
Group:		Applications/Graphics
Source0:	http://www.tomergabel.com/content/binary/PicasaWebDownloader12.zip
# Source0-md5:	e98b327af6fff08964aeb18fae1a0fc4
Patch0:		%{name}-imgmax.patch
URL:		http://www.tomergabel.com/PicasaWebDownloader.aspx
BuildRequires:	mono-csharp
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	mono
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PicasaWeb Downloader allows you to download albums from PicasaWeb site
without having to use (MS Windows-based) Picasa application.

%description -l pl.UTF-8
PicasaWeb Downloader pozwala ściągać albumy z serwisu PicasaWeb bez
potrzeby korzystania z aplikacji Picasa (przeznaczonej dla MS
Windows).

%prep
%setup -q -c
%undos Program.cs
%patch -P0 -p1

%build
gmcs -out:PicasaWebDownloader.exe Program.cs AssemblyInfo.cs

%install
rm -rf $RPM_BUILD_ROOT

install -D PicasaWebDownloader.exe $RPM_BUILD_ROOT%{_bindir}/PicasaWebDownloader.exe

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/PicasaWebDownloader.exe
