Summary:	PicasaWeb Downloader
Summary(pl.UTF-8):	Narzędzie do ściągania albumów z serwisu PicasaWeb
Name:		PicasaWebDownloader
Version:	1.1
Release:	1
License:	WTFPL
Group:		Applications/Graphics
Source0:	http://www.tomergabel.com/content/binary/PicasaWebDownloader11.zip
# Source0-md5:	3edba3a4973fce37c884b286a7e3e567
Patch0:		%{name}-url.patch
URL:		http://www.tomergabel.com/PicasaWeb+Downloader.aspx
BuildRequires:	mono-csharp
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
%patch0 -p1

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
