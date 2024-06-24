<div class="page-own-content">

<div class="page-row">
    <div class="page-title">
        <h3>Upload your CV</h3>

    </div>
</div>
<div class="page-row">
    <div class="page-title">
        <h3>
            <a href="{{ route('candidate.profile') }}" class="edit-link">back</a>
            Upload your CV
        </h3>
        @if (session('success'))
        <div class="da-alert da-alert-success" role="alert">
            {{ session('success') }}
            <button type="button" class="da-close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        @endif
    </div>
</div>
{{--  <div class="page-content">
    <div class="page-row">
        <div class="page-col">
            <div class="page-content-title">
                <p>Manage your profile below</p>
            </div>
        </div>
    </div>
</div>  --}}


<div class="profile-bio-container">
    <div class="profile-bio-wrapper">
        <div class="profile-cv-upload">
            <div class="profile-cv-upload-title">
                <h4>Upload your cv from your computer</h4>
            </div>
            <div class="profil-cv-upload-body">
                <form action="{{ route('candidate.profile.cv.submit') }}" method="POST" enctype="multipart/form-data">
                    @csrf
                    <div class="profile-form-row">
                        <div class="profile-form-group-col">
                            <label for="" class="profile-label" name="cv_upload">Choose</label>
                            <input type="file" name="cv_upload" class="profile-input">
                        </div>
                    </div>
                    <div class="profile-form-row">
                        <div class="profile-form-group-col">
                            <button class="btn btn-blue1" type="submit">Upload CV</button>
                        </div>
                    </div>
                </form>
            </div>

        </div>
    </div>
</div>

</div>
