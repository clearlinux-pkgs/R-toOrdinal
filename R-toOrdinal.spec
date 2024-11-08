#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-toOrdinal
Version  : 1.3.0.0
Release  : 42
URL      : https://cran.r-project.org/src/contrib/toOrdinal_1.3-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/toOrdinal_1.3-0.0.tar.gz
Summary  : Cardinal to Ordinal Number & Date Conversion
Group    : Development/Tools
License  : GPL-3.0
Requires: R-crayon
Requires: R-testthat
BuildRequires : R-crayon
BuildRequires : R-testthat
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n toOrdinal
cd %{_builddir}/toOrdinal

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645721967

%install
export SOURCE_DATE_EPOCH=1645721967
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library toOrdinal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library toOrdinal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library toOrdinal
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc toOrdinal || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/toOrdinal/CITATION
/usr/lib64/R/library/toOrdinal/DESCRIPTION
/usr/lib64/R/library/toOrdinal/INDEX
/usr/lib64/R/library/toOrdinal/Meta/Rd.rds
/usr/lib64/R/library/toOrdinal/Meta/features.rds
/usr/lib64/R/library/toOrdinal/Meta/hsearch.rds
/usr/lib64/R/library/toOrdinal/Meta/links.rds
/usr/lib64/R/library/toOrdinal/Meta/nsInfo.rds
/usr/lib64/R/library/toOrdinal/Meta/package.rds
/usr/lib64/R/library/toOrdinal/Meta/vignette.rds
/usr/lib64/R/library/toOrdinal/NAMESPACE
/usr/lib64/R/library/toOrdinal/NEWS
/usr/lib64/R/library/toOrdinal/R/toOrdinal
/usr/lib64/R/library/toOrdinal/R/toOrdinal.rdb
/usr/lib64/R/library/toOrdinal/R/toOrdinal.rdx
/usr/lib64/R/library/toOrdinal/doc/index.html
/usr/lib64/R/library/toOrdinal/doc/toOrdinal.R
/usr/lib64/R/library/toOrdinal/doc/toOrdinal.Rmd
/usr/lib64/R/library/toOrdinal/doc/toOrdinal.html
/usr/lib64/R/library/toOrdinal/help/AnIndex
/usr/lib64/R/library/toOrdinal/help/aliases.rds
/usr/lib64/R/library/toOrdinal/help/paths.rds
/usr/lib64/R/library/toOrdinal/help/toOrdinal.rdb
/usr/lib64/R/library/toOrdinal/help/toOrdinal.rdx
/usr/lib64/R/library/toOrdinal/html/00Index.html
/usr/lib64/R/library/toOrdinal/html/R.css
/usr/lib64/R/library/toOrdinal/tests/testthat.R
/usr/lib64/R/library/toOrdinal/tests/testthat/test_toOrdinalDate_english.R
/usr/lib64/R/library/toOrdinal/tests/testthat/test_toOrdinal_dutch.R
/usr/lib64/R/library/toOrdinal/tests/testthat/test_toOrdinal_english.R
/usr/lib64/R/library/toOrdinal/tests/testthat/test_toOrdinal_german.R
/usr/lib64/R/library/toOrdinal/tests/testthat/test_toOrdinal_swedish.R
